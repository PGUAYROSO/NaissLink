import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [utilisateur, setUtilisateur] = useState(null);
    const [token, setToken] = useState(
        localStorage.getItem("token")
    );

    async function login(accessToken, user) {

        localStorage.setItem("token", accessToken);

        setToken(accessToken);
        setUtilisateur(user);
    }

    function logout() {

        localStorage.removeItem("token");

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