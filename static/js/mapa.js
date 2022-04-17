import './ol/ol.css';
import Map from './ol/Map';
import OSM from './ol/source/OSM';
import TileLayer from './ol/layer/Tile';
import View from './ol/View';


const map = new Map({
    view: new View({
        //center:[0,0],
        //zoom: 0,

        center:[-37, -11],
        zoom: 8,            
    }),
    layers: [
        new TileLayer({
            source: new OSM(),
        }),           
    ],
    target: 'mapa',
    
});
$('.ol-full-screen').css('right','50px');

