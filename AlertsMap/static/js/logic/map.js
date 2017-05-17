function initMap() {


    map.leaflet = L.map('map', {
        center: conf.map.center
        , zoom: conf.map.zoom
        , minZoom: conf.map.minZoom
        , maxZoom: conf.map.maxZoom
        , maxBounds: conf.map.maxBounds
        , zoomControl: false
    });


    map.leaflet.on('viewreset', function() {
        map.leaflet.invalidateSize()
    });

    new L.Control.Zoom({ position: 'topright' }).addTo(map.leaflet)

    map.osmLayer = L.tileLayer(
        conf.map.tiles
        , {
            attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://osm.org/copyright">OpenStreetMap</a>'
        });

    map.leaflet.addLayer(map.osmLayer);

    map.ukrainianLayer = L.geoJson(null, {
        style: function(feature) {
            return {
                weight: 2
                , opacity: 1
                , color: '#aaa'
                // hide fill for Krym, Sevastopol, Donetsk and Luhansk
                , fill: ['0100000000', '8500000000', '1400000000', '4400000000'].indexOf(feature.properties['KOATUU']) == -1
                , fillColor: '#03f'
                , fillOpacity: .03
                , clickable: false
            }
        }
    });

    map.leaflet.addLayer(map.ukrainianLayer);

    d3.json('/static/data/oblasts.topojson', function (error, data) {
        var oblasts = topojson.feature(data, data.objects['oblasts']);
        map.ukrainianLayer.addData(oblasts);
    });

    map.raionsLayer = L.geoJson(null, {
        style: function(feature) {
            return {
                weight: 1
                , opacity: .3
                , color: '#aaa'
                , fill: true
                , fillColor: conf.raionColors[feature.properties['KOATUU']]
                , fillOpacity: .55
                , clickable: true
            }
        }
        , className: 'raions-overlay'
    });

    map.leaflet.addLayer(map.raionsLayer);

    map.greyZoneLayer = L.geoJson(conf.greyZone, {
        style: function(feature) {
            return {
                weight: 3
                , opacity: 0.6
                , color: 'rgb(238,88,89)'
                // , stroke: 'rgb(238,88,89)'
                , clickable: false
            }
        }
    });

    d3.json('/static/data/raion.topojson', function (error, data) {
        var donbas = topojson.feature(data, data.objects['raions']);
        map.raionsLayer.addData(donbas);
        map.leaflet.addLayer(map.greyZoneLayer);
    });


    return map;

}


/*=====  End of Init map  ======*/