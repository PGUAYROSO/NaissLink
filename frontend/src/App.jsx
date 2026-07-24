import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Dossiers from "./pages/Dossiers";
import Dossier from "./pages/Dossier";
import Transmissions from "./pages/Transmissions";
import Utilisateurs from "./pages/Utilisateurs";
import Parametres from "./pages/Parametres";
import TypesDocuments from "./pages/TypesDocuments";

import MainLayout from "./layouts/MainLayout";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {

    return (

        <BrowserRouter>

            <Routes>

                {/* -----------------------------
                    Login
                ----------------------------- */}

                <Route
                    path="/"
                    element={<Login />}
                />

                {/* -----------------------------
                    Routes protégées
                ----------------------------- */}

                <Route
                    element={
                        <ProtectedRoute>
                            <MainLayout />
                        </ProtectedRoute>
                    }
                >

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/dossiers"
                        element={<Dossiers />}
                    />

                    <Route
                        path="/dossiers/:numeroSejour"
                        element={<Dossier />}
                    />

                    <Route
                        path="/transmissions"
                        element={<Transmissions />}
                    />

                    <Route
                        path="/utilisateurs"
                        element={<Utilisateurs />}
                    />

                    <Route
                        path="/types-documents"
                        element={<TypesDocuments />}
                    />

                    <Route
                        path="/parametres"
                        element={<Parametres />}
                    />

                </Route>

            </Routes>

        </BrowserRouter>

    );

}

export default App;