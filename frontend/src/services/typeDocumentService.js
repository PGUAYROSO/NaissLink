import api from "../api/axios";

// ----------------------------------------------------
// Liste
// ----------------------------------------------------

export async function listerTypesDocuments() {

    const response = await api.get("/types-documents");

    return response.data;

}

// ----------------------------------------------------
// Consultation
// ----------------------------------------------------

export async function consulterTypeDocument(id) {

    const response = await api.get(`/types-documents/${id}`);

    return response.data;

}

// ----------------------------------------------------
// Création
// ----------------------------------------------------

export async function creerTypeDocument(data) {

    const response = await api.post(
        "/types-documents",
        data
    );

    return response.data;

}

// ----------------------------------------------------
// Modification
// ----------------------------------------------------

export async function modifierTypeDocument(id, data) {

    const response = await api.put(
        `/types-documents/${id}`,
        data
    );

    return response.data;

}

// ----------------------------------------------------
// Suppression
// ----------------------------------------------------

export async function supprimerTypeDocument(id) {

    await api.delete(
        `/types-documents/${id}`
    );

}