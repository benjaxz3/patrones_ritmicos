import streamlit as st

st.set_page_config(page_title="Idea de Investigación en Ciencia de Datos", layout="centered")

# -----------------------
# IMAGEN INICIAL
# -----------------------
st.markdown("""
<div style="display:flex; justify-content:center;">
    <img src="https://www.superprof.cl/blog/wp-content/uploads/2019/11/costo-primera-bateria.jpg"
         style="width:100%; max-height:400px; object-fit:cover; border-radius:10px;">
</div>
""", unsafe_allow_html=True)

    st.title("Análisis de Patrones Rítmicos de Batería")

    st.header("Área")
    st.write("Procesamiento de Audio (Ciencias de la Computación e Información) / ODS 4 Educacion de calidad y ODS 9 Industria, Innovación e Infraestructura")

    st.header("Idea de Investigación")
    st.write("""
    Uso de modelos de aprendizaje automático para analizar y clasificar patrones rítmicos de batería 
    en la música.
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
    
    st.title("Palabras Clave")
    
    st.subheader("Lista inicial")
    st.write("""
    - Patrones de bateria
    - Analisis de ritmos
    - Procesamiento de audio
    - Clasificacion de ritmos
    """)
    
    st.subheader("Expansión con IA")
    st.write("""
    - Drum pattern recognition
    - Rhythmic feature extraction
    - Machine learning
    - Tempo detection
    - Onset detection
    - Computational musicology
    - MIR (Music Information Retrieval)
    - Audio feature extraction
    - Deep learning for music analysis
    """)
    
    
