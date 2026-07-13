import api from "../api/axios";

export async function login(login, motDePasse) {
  const response = await api.post("/auth/login", {
    login,
    mot_de_passe: motDePasse,
  });

  return response.data;
}