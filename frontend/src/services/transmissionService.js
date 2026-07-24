import api from "../api/axios";

export async function creerTransmission(payload) {

    const { data } = await api.post(
        "/transmissions",
        payload
    );

    return data;

}

export async function listerTransmissions() {

    const { data } = await api.get("/transmissions");

    return data;

}

export async function receptionnerTransmission(id) {

    const { data } = await api.put(
        `/transmissions/${id}/receptionner`
    );

    return data;

}

export async function mettreEnInstruction(id) {

    const { data } = await api.put(
        `/transmissions/${id}/instruction`
    );

    return data;

}

export async function demanderComplement(id, commentaire) {

    const { data } = await api.put(
        `/transmissions/${id}/complement`,
        {
            commentaire
        }
    );

    return data;

}

export async function traiterTransmission(id) {

    const { data } = await api.put(
        `/transmissions/${id}/traiter`
    );

    return data;

}

export async function listerHistorique(id) {

    const response = await api.get(
        `/transmissions/${id}/historique`
    );

    return data;
}