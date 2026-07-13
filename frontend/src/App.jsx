import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

import MainLayout from "./layouts/MainLayout";
import ProtectedRoute from "./components/ProtectedRoute";

import Dossiers from "./pages/Dossiers";
import Transmissions from "./pages/Transmissions";
import Utilisateurs from "./pages/Utilisateurs";
import Parametres from "./pages/Parametres";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

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

        </Route>

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
        path="/transmissions"
        element={<Transmissions />}
    />

             <Route
        path="/utilisateurs"
        element={<Utilisateurs />}
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