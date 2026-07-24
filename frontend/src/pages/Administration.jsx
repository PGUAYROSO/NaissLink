import { useEffect, useState } from "react";
import axios from "axios";

export default function Administration() {
    const [infos, setInfos] = useState(null);

    useEffect(() => {
        axios.get("/api/administration/systeme")
            .then((res) => setInfos(res.data))
            .catch(console.error);
    }, []);

    if (!infos) {
        return <p>Chargement...</p>;
    }

    return (
        <div>
            <h1>Administration</h1>

            <table>
                <tbody>
                    <tr>
                        <td>Application</td>
                        <td>{infos.application}</td>
                    </tr>
                    <tr>
                        <td>Version</td>
                        <td>{infos.version}</td>
                    </tr>
                    <tr>
                        <td>Python</td>
                        <td>{infos.python}</td>
                    </tr>
                    <tr>
                        <td>Système</td>
                        <td>{infos.systeme}</td>
                    </tr>
                    <tr>
                        <td>Version OS</td>
                        <td>{infos.version_os}</td>
                    </tr>
                    <tr>
                        <td>Architecture</td>
                        <td>{infos.architecture}</td>
                    </tr>
                    <tr>
                        <td>Base de données</td>
                        <td>{infos.base_de_donnees}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}