import api from "../api/axios";

// Liste des dossiers
export async function listerDossiers() {

    const response = await api.get("/dossiers");

    return response.data;

}

// Consultation d'un dossier
export async function consulterDossier(numeroSejour) {

    const response = await api.get(
        `/dossiers/${numeroSejour}`
    );

    return response.data;

}

// Création d'un dossier
export async function creerDossier(numeroSejour) {

    const response = await api.post("/dossiers", {
        numero_sejour: numeroSejour
    });

    return response.data;

}