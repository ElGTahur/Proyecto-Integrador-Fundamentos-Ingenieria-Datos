# Evaluación 1 - Scraping de Noticias y Serialización en JSONL

## 📌 Fuente seleccionada
- **BBC Mundo** (https://www.bbc.com/mundo)  
Elegida por su facilidad de acceso y estructura HTML estable.

## 📂 Flujo de Adquisición de Datos
1. **Scraping** con `src/scraper.py`.  
2. **Serialización** en `data/raw/noticias.jsonl`.  
3. **Perfilado de calidad** en `reports/perfilado.md`.  
4. **Definición de contrato de datos** en `contracts/schema.yaml`.

## ⚙️ Ejecución
```bash
python src/scraper.py
```

## 📊 Archivos entregables
- `src/scraper.py` → código de scraping.  
- `data/raw/noticias.jsonl` → noticias extraídas.  
- `contracts/schema.yaml` → contrato de datos.  
- `reports/perfilado.md` → reporte de calidad.  
- `README.md` → documentación.  

## 🚧 Problemas encontrados
- BBC Mundo no siempre expone fecha ni autor en portada.  
- Se requiere extraer fecha del HTML interno de cada noticia si se quiere mayor calidad.  
