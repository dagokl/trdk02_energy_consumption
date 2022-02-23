import React, { useEffect, useState } from 'react';
import { IBuildingsData } from '../../types/interfaces';
import { getBuildings } from '../../services/buildingService';
import { Nav, NavLink, Bars, NavMenu } from './NavbarElements';
import SearchBar from './SearchBar';

const Navbar = () => {
  const [search, setSearch] = useState<IBuildingsData[]>([]);
  useEffect(() => {
    const fetchdata = async () => {
      const response: IBuildingsData[] = await getBuildings('');
      setSearch(response);
    };
    fetchdata();
  }, []);

  return (
    <>
      <Nav>
        <Bars />

        <NavMenu>
          <SearchBar data={search} />
          <NavLink to='/'>Homepage</NavLink>
          <NavLink to='/feature'>Feature</NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navbar;
