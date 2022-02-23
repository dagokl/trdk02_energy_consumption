export interface ICategory {
  id: string;
  name: string;
}

export interface IBuildingsData {
  id: string;
  name: string;
  year: number | null;
  area?: number;
  categoryIdEsave?: number;
  categoryDescription?: string;
  category: ICategory;
  tek?: string;
  energyLabel?: string;
}

export interface IBuilding {
  data: IBuildingsData;
}

export interface IBuildings {
  data: IBuildingsData[];
}
