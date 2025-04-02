def imputar_faltas(df, equipo_col, fouls_col):
    df_resultado = df.copy()
    equipos = df[equipo_col].unique()

    for equipo in equipos:
        # Filtro por equipo en su rol (local o visitante)
        mask_equipo = df[equipo_col] == equipo

        # Calcular la media de offsides cuando hay datos
        media_equipo = df.loc[mask_equipo & df[fouls_col].notnull(), fouls_col].mean()

        # Rellenar nulos con esa media
        df_resultado.loc[mask_equipo & df[fouls_col].isnull(), fouls_col] = media_equipo

    return df_resultado


def imputar_offsides(df, equipo_col, offside_col):
    df_resultado = df.copy()
    equipos = df[equipo_col].unique()

    for equipo in equipos:
        # Filtro por equipo en su rol (local o visitante)
        mask_equipo = df[equipo_col] == equipo

        # Calcular la media de offsides cuando hay datos
        media_equipo = df.loc[mask_equipo & df[offside_col].notnull(), offside_col].mean()

        # Rellenar nulos con esa media
        df_resultado.loc[mask_equipo & df[offside_col].isnull(), offside_col] = media_equipo

    return df_resultado