import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    gridItem: {
        alignItems: 'center',
        marginLeft: 'auto',
        marginRight: 'auto',
        marginTop: theme.spacing(2),
        paddingLeft: theme.spacing(1),
        paddingRight: theme.spacing(1),
    },
    extendWidth: {
        width: '100%',
    },
    mainGridContainer: {
        direction: 'column',
        alignItems: 'stretch',
    },
    paper: {
        padding: theme.spacing(3),
    },
    mainTitle: {
        borderBottomStyle: 'solid',
        borderBottomWidth: '2px',
        borderColor: theme.palette.grey[600],
        marginBottom: theme.spacing(1),
    },
    descTexts: {
        marginRight: '20%',
        [theme.breakpoints.down('xs')]: {
            marginRight: '0',
        },
    },
    subtitleInfoGrower: {
        flex: 1,
    },
    subtitleInfo: {
        marginBottom: theme.spacing(1),
    },
    subtitleInfoText: {
        lineHeight: 1.43,
    },
}));

export default useStyles;
