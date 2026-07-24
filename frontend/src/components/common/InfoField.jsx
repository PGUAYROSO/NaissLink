import {
    Stack,
    Typography
} from "@mui/material";

export default function InfoField({

    label,
    value

}) {

    return (

        <Stack
            direction="row"
            spacing={2}
            sx={{ mb: 1 }}
        >

            <Typography
                fontWeight="bold"
                width={180}
            >

                {label}

            </Typography>

            <Typography>

                {value || "-"}

            </Typography>

        </Stack>

    );

}