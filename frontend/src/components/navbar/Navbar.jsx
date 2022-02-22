import React from 'react';
import {
    Nav,
    NavLink,
    Bars,
    NavMenu,
} from './NavbarElements';

const Navbar = () => {
    return (
        <>
            <Nav>
                <Bars />

                <NavMenu>
                    <NavLink to='/' activeStyle>
                        Homepage
                    </NavLink>
                    <NavLink to='/feature' activeStyle>
                        Feature
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;