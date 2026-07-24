import {
    AppBar,
    Toolbar,
    Typography,
    Box,
    Avatar,
    IconButton,
    Menu,
    MenuItem,
    Divider
} from "@mui/material";

import {
    Logout,
    AccountCircle
} from "@mui/icons-material";

import { useState } from "react";

import { useAuth } from "../contexts/AuthContext";

export default function Header() {

    const { utilisateur, logout } = useAuth();

    const [anchorEl, setAnchorEl] = useState(null);

    const ouvrirMenu = (event) => {

        setAnchorEl(event.currentTarget);

    };

    const fermerMenu = () => {

        setAnchorEl(null);

    };

    return (

        <AppBar
            position="fixed"
            elevation={1}
            color="inherit"
            sx={{
                borderBottom: "1px solid #E0E0E0",
                color: "#333"
            }}
        >

            <Toolbar>

                <Typography
                    variant="h5"
                    sx={{
                        fontWeight: "bold",
                        color: "primary.main"
                    }}
                >
                    🩺 NaissLink
                </Typography>

                <Typography
                    sx={{
                        ml: 3,
                        color: "text.secondary"
                    }}
                >
                    Centre Hospitalier de la Basse-Terre
                </Typography>

                <Box sx={{ flexGrow: 1 }} />

                <Box
                    sx={{
                        display: "flex",
                        alignItems: "center",
                        cursor: "pointer"
                    }}
                    onClick={ouvrirMenu}
                >

                    <Avatar
                        sx={{
                            bgcolor: "primary.main",
                            width: 40,
                            height: 40,
                            mr: 2
                        }}
                    >
                        {utilisateur?.prenom?.charAt(0)}
                    </Avatar>

                    <Box>

                        <Typography
                            fontWeight="bold"
                            lineHeight={1.2}
                        >
                            {utilisateur?.prenom} {utilisateur?.nom}
                        </Typography>

                        <Typography
                            variant="caption"
                            color="text.secondary"
                        >
                            {utilisateur?.role}
                        </Typography>

                    </Box>

                    <IconButton>

                        <AccountCircle />

                    </IconButton>

                </Box>

                <Menu

                    anchorEl={anchorEl}

                    open={Boolean(anchorEl)}

                    onClose={fermerMenu}

                >

                    <MenuItem disabled>

                        <Box>

                            <Typography fontWeight="bold">

                                {utilisateur?.prenom} {utilisateur?.nom}

                            </Typography>

                            <Typography
                                variant="caption"
                            >

                                {utilisateur?.role}

                            </Typography>

                        </Box>

                    </MenuItem>

                    <Divider />

                    <MenuItem

                        onClick={() => {

                            fermerMenu();

                            logout();

                        }}

                    >

                        <Logout
                            fontSize="small"
                            sx={{ mr: 1 }}
                        />

                        Déconnexion

                    </MenuItem>

                </Menu>

            </Toolbar>

        </AppBar>

    );

}