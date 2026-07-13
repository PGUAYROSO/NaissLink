import {
    Drawer,
    Toolbar,
    List,
    ListItem,
    ListItemButton,
    ListItemText
} from "@mui/material";

import { Link } from "react-router-dom";

const drawerWidth = 240;

export default function Sidebar() {

    return (

        <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                "& .MuiDrawer-paper": {
                    width: drawerWidth,
                    boxSizing: "border-box"
                }
            }}
        >

            <Toolbar />

            <List>

                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/dashboard">
                        <ListItemText primary="🏠 Tableau de bord" />
                    </ListItemButton>
                </ListItem>

                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/dossiers">
                        <ListItemText primary="📁 Dossiers" />
                    </ListItemButton>
                </ListItem>

                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/transmissions">
                        <ListItemText primary="📤 Transmissions" />
                    </ListItemButton>
                </ListItem>

                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/utilisateurs">
                        <ListItemText primary="👥 Utilisateurs" />
                    </ListItemButton>
                </ListItem>

                <ListItem disablePadding>
                    <ListItemButton component={Link} to="/parametres">
                        <ListItemText primary="⚙ Paramètres" />
                    </ListItemButton>
                </ListItem>

            </List>

        </Drawer>

    );

}