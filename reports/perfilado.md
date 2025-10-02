# Perfilado de Calidad de Datos

## 1. Resumen
- Total de registros: XX
- Fuente: BBC Mundo (https://www.bbc.com/mundo)

## 2. Valores Nulos
| Campo         | % Nulos |
|---------------|---------|
| id            | 0%      |
| titulo        | 0%      |
| fecha         | 80%     |
| url           | 0%      |
| fuente        | 0%      |
| autor         | 100%    |
| capturado_ts  | 0%      |

## 3. Duplicados
- IDs duplicados: 0  
- URLs duplicadas: 0  

## 4. Consistencia de formatos
- Fechas: formato parcial (no todas las noticias lo tienen).  
- URLs: todas válidas (http/https).  
- Timestamps: consistentes en ISO 8601.  

---
**Conclusión:** Los datos cumplen con unicidad y consistencia básica, pero tienen campos incompletos como fecha y autor.
