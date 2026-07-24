import api from "../api/axios";

// ------------------------------------------------------------------
// Liste des documents d'un dossier
// ------------------------------------------------------------------

export async function listerDocuments(numeroSejour) {

    const response = await api.get(
        `/dossiers/${numeroSejour}/documents`
    );

    return response.data;

}

// ------------------------------------------------------------------
// Upload d'un document
// ------------------------------------------------------------------

export async function uploadDocument(formData) {

    const response = await api.post(
        "/documents/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }
    );

    return response.data;

}

// ------------------------------------------------------------------
// Prévisualisation d'un document
// ------------------------------------------------------------------

export async function visualiserDocument(documentId) {

    const response = await api.get(
        `/documents/${documentId}/download`,
        {
            responseType: "blob"
        }
    );

    return response.data;

}

// ------------------------------------------------------------------
// Téléchargement d'un document
// ------------------------------------------------------------------

export async function telechargerDocument(documentId) {

    const response = await api.get(
        `/documents/${documentId}/download`,
        {
            responseType: "blob"
        }
    );

    return response.data;

}

// ------------------------------------------------------------------
// Suppression d'un document
// ------------------------------------------------------------------

export async function supprimerDocument(documentId) {

    await api.delete(
        `/documents/${documentId}`
    );

}