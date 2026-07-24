import {
    Box,
    Typography,
    Button
} from "@mui/material";

export default function PageHeader({

    title,
    actionLabel,
    onAction

}) {

    return (

        <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            sx={{ mb: 3 }}
        >

            <Typography variant="h4">

                {title}

            </Typography>

            {

                actionLabel && (

                    <Button
                        variant="contained"
                        onClick={onAction}
                    >

                        {actionLabel}

                    </Button>

                )

            }

        </Box>

    );

}