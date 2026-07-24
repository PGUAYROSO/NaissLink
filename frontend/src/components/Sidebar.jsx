import {
    Drawer,
    Toolbar,
    List,
    ListItem,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Divider,
    Typography,
    Box
} from "@mui/material";

import {
    Dashboard,
    Folder,
    Send,
    Description,
    DocumentScanner,
    BarChart,
    People,
    Settings
} from "@mui/icons-material";

import { NavLink } from "react-router-dom";

const drawerWidth = 250;

const menuMetier = [

    {
        texte: "Tableau de bord",
        icone: <Dashboard />,
        lien: "/dashboard"
    },

    {
        texte: "Dossiers",
        icone: <Folder />,
        lien: "/dossiers"
    },

    {
        texte: "Transmissions",
        icone: <Send />,
        lien: "/transmissions"
    },

    {
        texte: "Documents",
        icone: <Description />,
        lien: "/documents"
    },

    {
        texte: "OCR",
        icone: <DocumentScanner />,
        lien: "/ocr"
    },

    {
        texte: "Statistiques",
        icone: <BarChart />,
        lien: "/statistiques"
    }

];

const menuAdmin = [

    {
        texte: "Utilisateurs",
        icone: <People />,
        lien: "/utilisateurs"
    },

    {
        texte: "Paramètres",
        icone: <Settings />,
        lien: "/parametres"
    }

];

export default function Sidebar() {

    return (

        <Drawer

            variant="permanent"

            sx={{

                width: drawerWidth,

                flexShrink: 0,

                "& .MuiDrawer-paper": {

                    width: drawerWidth,

                    boxSizing: "border-box",

                    borderRight: "1px solid #E0E0E0"

                }

            }}

        >

            <Toolbar />

            <Box sx={{ overflow: "auto" }}>

                <Typography
                    variant="overline"
                    sx={{
                        px: 3,
                        pt: 2,
                        color: "text.secondary"
                    }}
                >
                    MÉTIER
                </Typography>

                <List>

                    {menuMetier.map((item) => (

                        <ListItem
                            key={item.texte}
                            disablePadding
                        >

                            <ListItemButton

                                component={NavLink}

                                to={item.lien}

                                sx={{

                                    "&.active": {

                                        backgroundColor: "#E3F2FD",

                                        color: "primary.main",

                                        "& .MuiListItemIcon-root": {

                                            color: "primary.main"

                                        }

                                    }

                                }}

                            >

                                <ListItemIcon>

                                    {item.icone}

                                </ListItemIcon>

                                <ListItemText

                                    primary={item.texte}

                                />

                            </ListItemButton>

                        </ListItem>

                    ))}

                </List>

                <Divider sx={{ my: 2 }} />

                <Typography
                    variant="overline"
                    sx={{
                        px: 3,
                        color: "text.secondary"
                    }}
                >
                    ADMINISTRATION
                </Typography>

                <List>

                    {menuAdmin.map((item) => (

                        <ListItem
                            key={item.texte}
                            disablePadding
                        >

                            <ListItemButton

                                component={NavLink}

                                to={item.lien}

                                sx={{

                                    "&.active": {

                                        backgroundColor: "#E3F2FD",

                                        color: "primary.main",

                                        "& .MuiListItemIcon-root": {

                                            color: "primary.main"

                                        }

                                    }

                                }}

                            >

                                <ListItemIcon>

                                    {item.icone}

                                </ListItemIcon>

                                <ListItemText

                                    primary={item.texte}

                                />

                            </ListItemButton>

                        </ListItem>

                    ))}

                </List>

            </Box>

        </Drawer>

    );

}