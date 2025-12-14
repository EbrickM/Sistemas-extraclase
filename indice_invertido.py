# complete_app.py
import streamlit as st
import pandas as pd
import bisect
from collections import defaultdict
import re

class SimpleIndex:
    def __init__(self):
        self.index = defaultdict(list)
        self.stats = {"total_terms": 0, "total_docs": 0}
    
    def tokenize(self, text):
        """Tokenización simple"""
        return re.findall(r'\b\w+\b', text.lower())
    
    def add_document(self, doc_id, text):
        """Agregar documento usando arreglos ordenados"""
        terms = self.tokenize(text)
        for term in terms:
            if term not in self.index:
                self.index[term] = []
            postings = self.index[term]
            pos = bisect.bisect_left(postings, doc_id)
            if pos == len(postings) or postings[pos] != doc_id:
                bisect.insort(postings, doc_id)
        self.stats["total_docs"] = max(self.stats["total_docs"], doc_id)
    
    def fast_inv_build(self, documents):
        """Construcción rápida con Fast-Inv"""
        temp_index = defaultdict(list)
        for doc_id, text in enumerate(documents, 1):
            terms = self.tokenize(text)
            for term in terms:
                temp_index[term].append(doc_id)
        
        # Ordenar y eliminar duplicados
        for term in temp_index:
            self.index[term] = sorted(set(temp_index[term]))
        
        self.stats["total_docs"] = len(documents)
        self.stats["total_terms"] = len(self.index)
    
    def remove_term(self, term):
        """Eliminar un término del índice"""
        if term in self.index:
            del self.index[term]
            return True
        return False
    
    def get_statistics(self):
        """Obtener estadísticas del índice"""
        total_postings = sum(len(p) for p in self.index.values())
        return {
            "Términos únicos": len(self.index),
            "Total postings": total_postings,
            "Documentos": self.stats["total_docs"],
            "Promedio postings/ término": round(total_postings / max(1, len(self.index)), 2)
        }

def main():
    st.title("🔍 Herramienta de Indexado Invertido")
    st.markdown("---")
    
    # Inicializar índice en session_state
    if 'idx' not in st.session_state:
        st.session_state.idx = SimpleIndex()
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuración")
        
        method = st.radio(
            "Método de construcción:",
            ["Arreglos Ordenados", "Fast-Inv"],
            help="Arreglos: incremental, Fast-Inv: por lotes"
        )
        
        st.subheader("📥 Entrada de Datos")
        
        if method == "Arreglos Ordenados":
            doc_id = st.number_input("ID Documento", min_value=1, value=1)
            doc_text = st.text_area("Texto del documento")
            
            if st.button("Agregar Documento", type="primary"):
                st.session_state.idx.add_document(doc_id, doc_text)
                st.success(f"Documento {doc_id} indexado")
        
        else:  # Fast-Inv
            docs_input = st.text_area(
                "Documentos para Fast-Inv",
                placeholder="Ingrese un documento por línea\nEj:\nDocumento uno\nDocumento dos",
                height=150
            )
            
            if st.button("Construir Índice Fast-Inv"):
                documents = [d.strip() for d in docs_input.split('\n') if d.strip()]
                if documents:
                    st.session_state.idx.fast_inv_build(documents)
                    st.success(f"Índice construido con {len(documents)} documentos")
        
        st.subheader("🗑️ Operaciones")
        term_to_remove = st.text_input("Término a eliminar:")
        if st.button("Eliminar Término"):
            if st.session_state.idx.remove_term(term_to_remove.lower()):
                st.success(f"Término '{term_to_remove}' eliminado")
            else:
                st.warning("Término no encontrado")
    
    # Área principal
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header("📊 Estructura del Índice")
        
        if st.session_state.idx.index:
            # Crear tabla de datos
            data = []
            for term, postings in sorted(st.session_state.idx.index.items()):
                data.append({
                    "Término": term,
                    "Frecuencia": len(postings),
                    "Documentos": str(postings),
                    "Lista Postings": postings
                })
            
            df = pd.DataFrame(data)
            st.dataframe(
                df[["Término", "Frecuencia", "Documentos"]],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("El índice está vacío. Agrega documentos desde el panel lateral.")
    
    with col2:
        st.header("📈 Estadísticas")
        stats = st.session_state.idx.get_statistics()
        for key, value in stats.items():
            st.metric(label=key, value=value)
        
        # Búsqueda rápida
        st.subheader("🔎 Búsqueda")
        search_term = st.text_input("Buscar término:")
        if search_term:
            postings = st.session_state.idx.index.get(search_term.lower(), [])
            if postings:
                st.success(f"Encontrado en documentos: {postings}")
            else:
                st.error("Término no encontrado")
    
    # Información adicional
    with st.expander("ℹ️ Acerca de esta herramienta"):
        st.markdown("""
        **Características implementadas:**
        
        1. ✅ Indexado por arreglos ordenados (usando `bisect`)
        2. ✅ Algoritmo Fast-Inv para construcción por lotes
        3. ✅ Visualización clara de la estructura del índice
        4. ✅ Eliminación eficiente de términos
        5. ✅ Estadísticas básicas
        6. ✅ Búsqueda interactiva
        
        **Uso:**
        - Usa **Arreglos Ordenados** para indexar documentos de uno en uno
        - Usa **Fast-Inv** para indexar múltiples documentos a la vez
        - Los términos se tokenizan automáticamente (minúsculas, solo palabras)
        """)

if __name__ == "__main__":
    main()