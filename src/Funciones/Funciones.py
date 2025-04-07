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


# Determinar quién metió el primer gol basado en los minutos
def quien_anoto_primero(row):
    h = row['minuto_gol_home']
    a = row['minuto_gol_away']
    
    if pd.isna(h) and pd.isna(a):
        return 'ninguno'
    elif pd.isna(h):
        return 'away'
    elif pd.isna(a):
        return 'home'
    else:
        return 'home' if h < a else 'away' if a < h else 'simultaneo'
    

def extraer_minuto(texto):
    if pd.isna(texto) or texto.strip() == '':
        return np.nan
    try:
        # Usa regex para extraer todos los numeritos del string
        minutos = [int(s) for s in re.findall(r'\d+', texto)]
        return min(minutos) if minutos else np.nan
    except:
        return np.nan
