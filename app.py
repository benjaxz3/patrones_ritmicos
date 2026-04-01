import streamlit as st

st.set_page_config(page_title="Idea de Investigación en Ciencia de Datos", layout="wide")

st.title("Análisis de Patrones Rítmicos de Batería")

st.header("Área")
st.write("Procesamiento de Audio")

st.header("Idea de Investigación")
st.write("""
Uso de modelos de aprendizaje automático para analizar y clasificar patrones rítmicos de batería 
en música moderna mediante técnicas de procesamiento de audio y extracción de características.
""")

st.header("Fundamento o Motivación")
st.write("""
La batería es el elemento central del ritmo en muchos géneros musicales. Sin embargo, el análisis 
del estilo rítmico suele depender principalmente de la percepción humana. Mediante técnicas de 
Ciencia de Datos y procesamiento de audio es posible extraer características rítmicas automáticamente 
y analizar patrones de ejecución entre distintos bateristas o géneros musicales.
""")

st.header("Descripción del Problema")
st.write("""
Actualmente existen grandes colecciones de música digital, pero el análisis automático del estilo 
rítmico de baterías sigue siendo limitado. Identificar patrones característicos de ejecución podría 
permitir clasificar géneros musicales, detectar estilos de bateristas o incluso generar nuevos 
ritmos mediante modelos de aprendizaje automático.
""")

st.header("Relevancia")
st.write("""
Esta investigación es relevante porque conecta la Ciencia de Datos con el análisis musical 
computacional. Sus resultados podrían aplicarse en sistemas de recomendación musical, herramientas 
educativas para músicos o generación automática de ritmos en producción musical.
""")

st.header("Palabras Clave")

st.subheader("Lista inicial")
st.write("""
- Drum patterns
- Rhythm analysis
- Music data mining
- Audio signal processing
- Machine learning for music
- Beat detection
- Rhythm classification
- Music information retrieval
""")

st.subheader("Expansión con IA")
st.write("""
- Drum pattern recognition
- Rhythmic feature extraction
- Tempo detection
- Onset detection
- Computational musicology
- MIR (Music Information Retrieval)
- Audio feature extraction
- Deep learning for music analysis
""")

st.success("Proyecto propuesto para investigación en Ciencia de Datos aplicada a análisis musical.")
