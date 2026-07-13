import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        primary: {
            main: "#1565C0"
        },

        secondary: {
            main: "#2E7D32"
        },

        success: {
            main: "#2E7D32"
        },

        warning: {
            main: "#ED6C02"
        },

        error: {
            main: "#D32F2F"
        },

        background: {

            default: "#F5F7FA",

            paper: "#FFFFFF"

        }

    },

    typography: {

        fontFamily: [
            "Roboto",
            "Arial",
            "sans-serif"
        ].join(","),

        h4: {

            fontWeight: 700

        }

    },

    shape: {

        borderRadius: 10

    }

});

export default theme;