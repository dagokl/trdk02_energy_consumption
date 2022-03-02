import React from 'react';
import classNames from 'classnames';
import { Grid, Box, Card, Typography, Paper } from '@material-ui/core';
import SelectedBuilding from './../styles/SelectedBuilding.js';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine } from 'recharts';


const data = [
    {
        name: '22.02.22',
        Fjernvarme: 4000,
        Resterende: 2400,
        amt: 2400,
    },
    {
        name: '23.02.22',
        Fjernvarme: 3000,
        Resterende: 1398,
        amt: 2210,
    },
    {
        name: '24.02.22',
        Fjernvarme: 2000,
        Resterende: 9800,
        amt: 2290,
    },
    {
        name: '25.02.22',
        Fjernvarme: 2780,
        Resterende: 3908,
        amt: 2000,
    },
    {
        name: '26.02.22',
        Fjernvarme: 1890,
        Resterende: 4800,
        amt: 2181,
    },
    {
        name: '27.02.22',
        Fjernvarme: 2390,
        Resterende: 13800,
        amt: 2500,
    },
    {
        name: '28.02.22',
        Fjernvarme: 3490,
        Resterende: 4300,
        amt: 2100,
    },
    {
        name: '01.03.22',
        Fjernvarme: 4000,
        Resterende: 2400,
        amt: 2400,
    },
    {
        name: '02.03.22',
        Fjernvarme: 3000,
        Resterende: 1398,
        amt: 2210,
    },
    {
        name: '03.03.22',
        Fjernvarme: 2000,
        Resterende: 9800,
        amt: 2290,
    },
    {
        name: '04.03.22',
        Fjernvarme: 2780,
        Resterende: 3908,
        amt: 2000,
    },
    {
        name: '05.03.22',
        Fjernvarme: 1890,
        Resterende: 4800,
        amt: 2181,
    },
    {
        name: '06.03.22',
        Fjernvarme: 2390,
        Resterende: 13800,
        amt: 2500,
    },
    {
        name: '07.03.22',
        Fjernvarme: 3490,
        Resterende: 4300,
        amt: 2100,
    },
    {
        name: '08.03.22',
        Fjernvarme: 4000,
        Resterende: 2400,
        amt: 2400,
    },
    {
        name: '09.03.22',
        Fjernvarme: 3000,
        Resterende: 1398,
        amt: 2210,
    },
    {
        name: '10.03.22',
        Fjernvarme: 2000,
        Resterende: 9800,
        amt: 2290,
    },
    {
        name: '11.03.22',
        Fjernvarme: 2780,
        Resterende: 3908,
        amt: 2000,
    },
    {
        name: '12.03.22',
        Fjernvarme: 1890,
        Resterende: 4800,
        amt: 2181,
    },
    {
        name: '13.03.22',
        Fjernvarme: 2390,
        Resterende: 13800,
        amt: 2500,
    },
    {
        name: '14.03.22',
        Fjernvarme: 3490,
        Resterende: 4300,
        amt: 2100,
    },
];

const classesP = SelectedBuilding();


const Feature = () => {
    return (
        <Box>
            <Grid container className={classesP.mainGridContainer}>
                <Grid item xs={12} className={classesP.extendWidth}></Grid>
                <Grid
                    item
                    xs={12}
                    sm={8}
                    fullWidth
                    className={classNames(classesP.gridItem)}
                >
                    <Paper
                        className={classNames(classesP.paper)}
                        elevation={4}
                    >

                    </Paper>

                    <Card>
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
                            <Tooltip label="Kug" />
                            <ReferenceLine y={11100} stroke="red" />
                            <Legend />
                            <Bar dataKey="Fjernvarme" stackId="a" fill="#8884d8" />
                            <Bar dataKey="Resterende" stackId="a" fill="#82ca9d" />
                        </BarChart>
                    </Card>
                </Grid>
                <Grid
                    item
                    xs={12}
                    sm={8}
                    fullWidth
                    className={classNames(classesP.gridItem)}
                >
                    <Paper
                        className={classNames(classesP.paper)}
                        elevation={4}
                    >
                    </Paper>
                    <Typography
                        gutterBottom
                        variant="h5"
                        component="h2"
                        className={classesP.mainTitle}
                    >
                        Barnehagen Skole
            </Typography>
                    <Grid container className={classesP.subtitleInfo}>
                        <Grid item xs={12}>
                            <Typography
                                variant="overline"
                                display="block"
                                gutterBottom
                                className={classesP.subtitleInfoText}
                            >
                                Bygningstype: Skole
                </Typography>
                        </Grid>
                        <Grid item className={classesP.subtitleInfoGrower}>
                            <Typography
                                variant="overline"
                                display="block"
                                className={classesP.subtitleInfoText}
                            >
                                Forventet årlig energiforbruk: 182312 kWh
                </Typography>
                        </Grid>
                        <Grid item className={classesP.subtitleInfoGrower}>
                            <Typography
                                variant="overline"
                                display="block"
                                className={classesP.subtitleInfoText}
                            >
                                Adresse: Barnehageskoleveien 69
                            </Typography>
                        </Grid>
                    </Grid>
                    <Typography gutterBottom variant="h6" component="h3">
                        Beskrivelse:{' '}
                    </Typography>
                    <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                        className={classesP.descTexts}
                    >
                        Skole med 420 elever
                    </Typography>
                </Grid>
            </Grid>
        </Box>
    );
};

export default Feature;