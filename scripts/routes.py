from base import Base
from typing import List, Optional
import pandas as pd
import numpy as np

class Routes(Base):
    def __init__(self, filename="bus_routes.csv", data_folder="../data/output_tables"):
        super().__init__(filename=filename, data_folder=data_folder)

    def term_dest(self, **kwargs) -> pd.DataFrame:
        return self.destinations('term.', **kwargs)
    
    def metro_dest(self, **kwargs) -> pd.DataFrame:
        return self.destinations('metrô', **kwargs)

    def train_dest(self, **kwargs) -> pd.DataFrame:
        return self.destinations('cptm', **kwargs)

    def destinations(self,
                 dest: str,
                 areaids: Optional[List[int]] = None,
                 route_code: Optional[List[str]] = None,
                 extreme: bool = False) -> pd.DataFrame:
    
        dest = dest.lower()  # transforma em minúsculas para ignorar a diferença de maiúsculas e minúsculas
        conditions = [self.df['route_long_name'].str.lower().str.contains(dest)]
        
        if extreme:
            conditions.append(self.df['route_long_name'].str.lower().str.count(dest).eq(2))
        
        if areaids is not None:
            conditions.append(self.df['route_areaid'].isin(areaids))
        
        if route_code is not None:
            conditions.append(self.df['route_code'].isin(route_code))
        
        conditions.append(self.df['direction_id'].eq(0))
        result = self.df[np.all(conditions, axis=0)]
        
        if len(result) == 0:
            print(f"Nenhuma rota com destino a '{dest}' encontrada.")
    
        return result