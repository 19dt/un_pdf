import streamlit as st
import PyPDF2

# Variables
output_pdf = "documents/pdf_final.pdf"


# Functions
def join_pdfs(output_path, documents):
    # Creamos un objeto PdfMerger de PyPDF2 para combinar archivos PDF
    pdf_final = PyPDF2.PdfMerger()
    
    for document in documents:
        pdf_final.append(document)
        
    pdf_final.write(output_path) # Guardamos el pdf combinado en la ruta de salida




# FRONT

st.image("assets/combine-pdf.png")
st.header("Unir PDF")
st.subheader("Adjuntar pdfs para unir")

pdf_adjuntos = st.file_uploader(label="", accept_multiple_files=True)

unir = st.button(label="Unir PDFs") # Creamos boton llamado "Unir PDFs"

if unir:
    if len(pdf_adjuntos) <=1:
        st.warning("Debes adjuntar más de un PDF")
        
    else:
        join_pdfs(output_pdf, pdf_adjuntos)
        st.success("Desde aquí puede descargar el PDF final")
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label="Descargar PDF final", data=pdf_data, file_name="pdf_final.pdf")