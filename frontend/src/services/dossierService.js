import api from "../api/axios";

export async function listerDossiers() {

    const response = await api.get("/dossiers");

    return response.data;

}