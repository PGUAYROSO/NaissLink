import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [token, setToken] = useState(
        localStorage.getItem("token")
    );

    const [utilisateur, setUtilisateur] = useState(() => {

        const data = localStorage.getItem("utilisateur");

        return data ? JSON.parse(data) : null;

    });

    function login(accessToken, user) {

        localStorage.setItem("token", accessToken);

        localStorage.setItem(
            "utilisateur",
            JSON.stringify(user)
        );

        setToken(accessToken);
        setUtilisateur(user);

    }

    function logout() {

        localStorage.removeItem("token");
        localStorage.removeItem("utilisateur");

        setToken(null);
        setUtilisateur(null);

    }

    return (

        <AuthContext.Provider
            value={{
                utilisateur,
                token,
                login,
                logout
            }}
        >

            {children}

        </AuthContext.Provider>

    );

}

export function useAuth() {
    return useContext(AuthContext);
}