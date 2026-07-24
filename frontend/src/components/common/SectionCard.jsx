import {
    Paper,
    Typography,
    Divider,
    Box
} from "@mui/material";

export default function SectionCard({

    title,
    children

}) {

    return (

        <Paper
            elevation={2}
            sx={{ p: 3 }}
        >

            <Typography
                variant="h6"
                gutterBottom
            >
                {title}
            </Typography>

            <Divider sx={{ mb: 2 }} />

            <Box>

                {children}

            </Box>

        </Paper>

    );

}