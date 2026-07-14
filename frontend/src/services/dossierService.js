import api from "../api/axios";

export async function listerDossiers() {

    const response = await api.get("/dossiers");

    return response.data;

}
export async function creerDossier(numeroSejour) {

    const response = await api.post("/dossiers", {

        numero_sejour: numeroSejour

    });

    return response.data;

}