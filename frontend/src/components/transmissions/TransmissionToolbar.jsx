import {
    Stack,
    TextField,
    InputAdornment
} from "@mui/material";

import SearchIcon from "@mui/icons-material/Search";

export default function TransmissionToolbar({
    recherche,
    setRecherche,
}) {

    return (

        <Stack
            direction="row"
            justifyContent="space-between"
            alignItems="center"
            spacing={2}
            sx={{ mb: 3 }}
        >

            <TextField
                placeholder="Rechercher une transmission..."
                size="small"
                value={recherche}
                onChange={(e) => setRecherche(e.target.value)}
                sx={{ width: 380 }}
                InputProps={{
                    startAdornment: (
                        <InputAdornment position="start">
                            <SearchIcon />
                        </InputAdornment>
                    )
                }}
            />

        </Stack>

    );

}