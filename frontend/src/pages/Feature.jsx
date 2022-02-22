import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid } from 'recharts';

const data = [
    {
        name: 'Page A',
        uv: 4000,
        pv: 2400,
        amt: 2400,
    },
    {
        name: 'Page B',
        uv: 3000,
        pv: 1398,
        amt: 2210,
    },
    {
        name: 'Page C',
        uv: 2000,
        pv: 9800,
        amt: 2290,
    },
    {
        name: 'Page D',
        uv: 2780,
        pv: 3908,
        amt: 2000,
    },
    {
        name: 'Page E',
        uv: 4000,
        pv: 2400,
        amt: 2400,
    },
    {
        name: 'Page F',
        uv: 3000,
        pv: 1398,
        amt: 2210,
    },
    {
        name: 'Page G',
        uv: 2000,
        pv: 9800,
        amt: 2290,
    },
    {
        name: 'Page H',
        uv: 2780,
        pv: 3908,
        amt: 2000,
    },
];

const Feature = () => {
    return (
        <LineChart width={500} height={300} data={data}>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
            <Line type="monotone" dataKey="uv" stroke="#8884d8" />
            <Line type="monotone" dataKey="pv" stroke="#82ca9d" />
        </LineChart>
    );
};

export default Feature;