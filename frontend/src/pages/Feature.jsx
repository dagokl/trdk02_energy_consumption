import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';


const data = [
    {
        name: 'Page A',
        Fjernvarme: 4000,
        Resterende: 2400,
        amt: 2400,
    },
    {
        name: 'Page B',
        Fjernvarme: 3000,
        Resterende: 1398,
        amt: 2210,
    },
    {
        name: 'Page C',
        Fjernvarme: 2000,
        Resterende: 9800,
        amt: 2290,
    },
    {
        name: 'Page D',
        Fjernvarme: 2780,
        Resterende: 3908,
        amt: 2000,
    },
    {
        name: 'Page E',
        Fjernvarme: 1890,
        Resterende: 4800,
        amt: 2181,
    },
    {
        name: 'Page F',
        Fjernvarme: 2390,
        Resterende: 13800,
        amt: 2500,
    },
    {
        name: 'Page G',
        Fjernvarme: 3490,
        Resterende: 4300,
        amt: 2100,
    },
];

const Feature = () => {
    return (
        <BarChart
            width={500}
            height={300}
            data={data}
            margin={{
                top: 20,
                right: 30,
                left: 20,
                bottom: 5,
            }}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="Fjernvarme" stackId="a" fill="#8884d8" />
            <Bar dataKey="Resterende" stackId="a" fill="#82ca9d" />
        </BarChart>
    );
};

export default Feature;