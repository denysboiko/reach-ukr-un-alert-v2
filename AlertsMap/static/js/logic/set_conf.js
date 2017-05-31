var raionColors = {
    '1410100000': '#51a9ff',
    '1410200000': '#33ccff',
    '1410300000': '#42bbff',
    '1410600000': '#4282ff',
    '1410900000': '#23e2ff',
    '1411200000': '#b8e2fd',
    '1413200000': '#51a9ff',
    '1413300000': '#33ccff',
    '1413500000': '#42bbff',
    '1413600000': '#4282ff',
    '1413800000': '#23e2ff',
    '1414100000': '#b8e2fd',
    '1414400000': '#51a9ff',
    '1414700000': '#33ccff',
    '1414800000': '#42bbff',
    '1415000000': '#4282ff',
    '1422700000': '#b8e2fd',
    '1423000000': '#23e2ff',
    '1423300000': '#33ccff',
    '1423600000': '#51a9ff',
    '1423900000': '#42bbff',
    '1424200000': '#4282ff',
    '1424500000': '#23e2ff',
    '1424800000': '#b8e2fd',
    '1425200000': '#b8e2fd',
    '1425500000': '#23e2ff',
    '1415300000': '#42bbff',
    '1415500000': '#4282ff',
    '1420300000': '#51a9ff',
    '1420600000': '#33ccff',
    '1420900000': '#b8e2fd',
    '1421200000': '#4282ff',
    '1421500000': '#42bbff',
    '1421700000': '#33ccff',
    '1422000000': '#23e2ff',
    '1422400000': '#51a9ff',
    '1411300000': '#42bbff',
    '1411500000': '#33ccff',
    '1411600000': '#4282ff',
    '1411700000': '#b8e2fd',
    '1412000000': '#51a9ff',
    '1412100000': '#23e2ff',
    '1412300000': '#4282ff',
    '1412500000': '#51a9ff',
    '1412600000': '#23e2ff',
    '1412900000': '#33ccff',
    '4410100000': '#42bbff',
    '4410300000': '#b8e2fd',
    '4410500000': '#51a9ff',
    '4411000000': '#33ccff',
    '4411200000': '#42bbff',
    '4411400000': '#4282ff',
    '4411600000': '#23e2ff',
    '4411800000': '#b8e2fd',
    '4412100000': '#51a9ff',
    '4412300000': '#42bbff',
    '4412500000': '#33ccff',
    '4412700000': '#4282ff',
    '4412900000': '#23e2ff',
    '4413100000': '#b8e2fd',
    '4420300000': '#33ccff',
    '4420600000': '#42bbff',
    '4420900000': '#23e2ff',
    '4421400000': '#51a9ff',
    '4421600000': '#4282ff',
    '4422200000': '#b8e2fd',
    '4422500000': '#23e2ff',
    '4422800000': '#51a9ff',
    '4423100000': '#b8e2fd',
    '4423300000': '#33ccff',
    '4423600000': '#4282ff',
    '4423800000': '#42bbff',
    '4424000000': '#42bbff',
    '4424200000': '#33ccff',
    '4424500000': '#23e2ff',
    '4424800000': '#4282ff',
    '4425100000': '#51a9ff',
    '4425400000': '#b8e2fd'
};

function setConf(data_url, full_access) {

    var tiles_list = {
        ru: 'https://api.mapbox.com/styles/v1/denysboiko/cj31bg47c00072rqpzul3t1qb/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        ua: 'https://api.mapbox.com/styles/v1/denysboiko/cj31bi4rk000b2socgh8kzaeu/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        en: 'https://api.mapbox.com/styles/v1/denysboiko/cj1hz2pno004g2qk8fbfwqrtc/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        osm: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png'
    };

    return {
        map: {
            tiles: tiles_list[window.localStorage['lang']]
            , center: [48.1, 38.2]
            , zoom: 8
            , minZoom: 6
            , maxZoom: 18
            , maxBounds: [
                [44 - 2, 22] // south coords of ukraine + space to bottom datepicker, Ukraine west
                , [53 + 4, 41 + 16] // Ukraine north + some space to popups, east coords of ukraine + space to make center near Donetsk/Luhansk on minZoom
            ]
        }
        //, admUkrainian: window.adm1
        //, admRaions: window.raionsDonetskLuhansk

        , dateFormat: d3.time.format('%e %b %Y')
        , dateFormatString: '%e %b %Y'
        , dateFormatShort: d3.time.format('%b %y')
        , dateFormatShortString: '%b %y'
        , dateParse: d3.time.format('%Y-%m-%d')
        , markerMinDiam: 20
        , markerMaxDiam: 50
        , markerSpacer: 20
        , paginationStep: 15
        , tplPopup: _.template(d3.select('#tplPopup').html())
        , tplDataTableRow: _.template(d3.select('#tplDataTableRow').html())
        , tplDataTableHead: _.template(d3.select('#tplDataTableHead').html())
        , tplFilterCounter: _.template(d3.select('#tplFilterCounter').html())
        , greyZone: window.greyZone
        , data: {
            referals: {
                urls: ['/alerts?format=json']
                , loader: d3.json
                , fields: {
                      settlement: 'settlement'
                    , oblast: 'oblast'
                    , raion: 'raion'
                    , raionCode: 'raionCode'
                    , latitude: 'latitude'
                    , longitude: 'longitude'
                    , affected: 'no_affected'
                    , date: 'date_referal'
                    , status: 'status'
                    , clusters: 'clusters'
                    , partners: 'response_partners'
                    , type: 'type'
                    , needs: 'need_types'
                    , covered: 'no_beneficiaries'
                    , context: 'context'
                    , description: 'description'
                    , infoLink: 'additional_info_link'
                    , conflictRelated: 'conflict_related'
                    , items: 'items'
                    , responses: 'responses'
                    , view_url: 'view_url'

                },
                full_access: full_access
            }
        }
        , filterStatus: [
              {key: 'Resolved', text: 'Resolved', color: '#70A800'}
            , {key: 'Addressed But Unresolved', text: 'Addressed, not resolved', color: '#F69E61'}
            , {key: 'Not Addressed', text: 'Not addressed', color: '#EE5859'}
        ]
        // , filterCluster: clusters
        , filterOblast: {
            // keyInSourceCode: 'Key data in document'
            donetsk: 'Donetska'
            , luhansk: 'Luhanska'
        }
        , filterOblastRaions: {
            donetsk: [
                {key: '1420600000', value: 'Amvrosiivskyi'}, {key: '1410300000', value: 'Artemivska'}
                , {key: '1410200000', value: 'Avdiivska'}, {key: '1420900000', value: 'Bakhmutskyi'}
                , {key: '1410900000', value: 'Debaltsevcka'}, {key: '1411500000', value: 'Dobropilska'}
                , {key: '1422000000', value: 'Dobropilskyi'}, {key: '1411600000', value: 'Dokuchaievska'}
                , {key: '1410100000', value: 'Donetska'}, {key: '1411700000', value: 'Druzhkivska'}
                , {key: '1411300000', value: 'Dymytrivska'}, {key: '1411200000', value: 'Dzerzhynska'}
                , {key: '1410600000', value: 'Horlivska'}, {key: '1415000000', value: 'Khartsyzka'}
                , {key: '1412500000', value: 'Kirovska'}, {key: '1412600000', value: 'Kostiantynivska'}
                , {key: '1422400000', value: 'Kostiantynivskyi'}, {key: '1412900000', value: 'Kramatorska'}
                , {key: '1413200000', value: 'Krasnoarmiiska'}, {key: '1422700000', value: 'Krasnoarmiiskyi'}
                , {key: '1413300000', value: 'Krasnolymanska'}, {key: '1423000000', value: 'Krasnolymanskyi'}
                , {key: '1413500000', value: 'Makiivska'}, {key: '1423300000', value: 'Marinskyi'}
                , {key: '1412300000', value: 'Mariupolska'}, {key: '1423600000', value: 'Novoazovskyi'}
                , {key: '1413600000', value: 'Novohrodivska'}, {key: '1420300000', value: 'Oleksandrivskyi'}
                , {key: '1423900000', value: 'Pershotravnevyi'}, {key: '1413800000', value: 'Selydivska'}
                , {key: '1415300000', value: 'Shakhtarska'}, {key: '1425200000', value: 'Shakhtarskyi'}
                , {key: '1414100000', value: 'Slovianska'}, {key: '1424200000', value: 'Slovianskyi'}
                , {key: '1414400000', value: 'Snizhnianska'}, {key: '1424500000', value: 'Starobeshivskyi'}
                , {key: '1424800000', value: 'Telmanivskyi'}, {key: '1414700000', value: 'Torezka'}
                , {key: '1421200000', value: 'Velykonovosilkivskyi'}, {key: '1421500000', value: 'Volnovaskyi'}
                , {key: '1421700000', value: 'Volodarskyi'}, {key: '1414800000', value: 'Vuhledarska'}
                , {key: '1415500000', value: 'Yasynuvatska'}, {key: '1425500000', value: 'Yasynuvatskyi'}
                , {key: '1412000000', value: 'Yenakiivska'}, {key: '1412100000', value: 'Zhdanivska'}
            ]
            //'http://127.0.0.1:4000/filter/alert_system/Raion/oblast/alert_system/Alert/raion/1400000000/'
            , luhansk: [
                {key: '4411200000', value: 'Alchevska'}, {key: '4420300000', value: 'Antratsytivskyi'}
                , {key: '4410300000', value: 'Antratsytska'}, {key: '4420900000', value: 'Bilokurakynskyi'}
                , {key: '4420600000', value: 'Bilovodskyi'}, {key: '4410500000', value: 'Briankivska'}
                , {key: '4411000000', value: 'Kirovska'}, {key: '4411400000', value: 'Krasnodonska'}
                , {key: '4421400000', value: 'Krasnodonskyi'}, {key: '4411600000', value: 'Krasnolutska'}
                , {key: '4421600000', value: 'Kreminskyi'}, {key: '4410100000', value: 'Luhanska'}
                , {key: '4422200000', value: 'Lutuhynskyi'}, {key: '4411800000', value: 'Lysychanska'}
                , {key: '4422500000', value: 'Markivskyi'}, {key: '4422800000', value: 'Milovskyi'}
                , {key: '4423100000', value: 'Novoaidarskyi'}, {key: '4423300000', value: 'Novopskovskyi'}
                , {key: '4423600000', value: 'Perevalskyi'}, {key: '4412100000', value: 'Pervomaiska'}
                , {key: '4423800000', value: 'Popasnianskyi'}, {key: '4412300000', value: 'Rovenkivska'}
                , {key: '4412500000', value: 'Rubizhanska'}, {key: '4412900000', value: 'Sievierodonetska'}
                , {key: '4424500000', value: 'Slovianoserbskyi'}, {key: '4413100000', value: 'Stakhanovska'}
                , {key: '4424800000', value: 'Stanychno-Luhanskyi'}, {key: '4425100000', value: 'Starobilskyi'}
                , {key: '4424000000', value: 'Svativskyi'}, {key: '4412700000', value: 'Sverdlovska'}
                , {key: '4424200000', value: 'Sverdlovskyi'}, {key: '4425400000', value: 'Troitskyi'}
            ]
        }

        , raionColors: {
            '1410100000': '#51a9ff',
            '1410200000': '#33ccff',
            '1410300000': '#42bbff',
            '1410600000': '#4282ff',
            '1410900000': '#23e2ff',
            '1411200000': '#b8e2fd',
            '1413200000': '#51a9ff',
            '1413300000': '#33ccff',
            '1413500000': '#42bbff',
            '1413600000': '#4282ff',
            '1413800000': '#23e2ff',
            '1414100000': '#b8e2fd',
            '1414400000': '#51a9ff',
            '1414700000': '#33ccff',
            '1414800000': '#42bbff',
            '1415000000': '#4282ff',
            '1422700000': '#b8e2fd',
            '1423000000': '#23e2ff',
            '1423300000': '#33ccff',
            '1423600000': '#51a9ff',
            '1423900000': '#42bbff',
            '1424200000': '#4282ff',
            '1424500000': '#23e2ff',
            '1424800000': '#b8e2fd',
            '1425200000': '#b8e2fd',
            '1425500000': '#23e2ff',
            '1415300000': '#42bbff',
            '1415500000': '#4282ff',
            '1420300000': '#51a9ff',
            '1420600000': '#33ccff',
            '1420900000': '#b8e2fd',
            '1421200000': '#4282ff',
            '1421500000': '#42bbff',
            '1421700000': '#33ccff',
            '1422000000': '#23e2ff',
            '1422400000': '#51a9ff',
            '1411300000': '#42bbff',
            '1411500000': '#33ccff',
            '1411600000': '#4282ff',
            '1411700000': '#b8e2fd',
            '1412000000': '#51a9ff',
            '1412100000': '#23e2ff',
            '1412300000': '#4282ff',
            '1412500000': '#51a9ff',
            '1412600000': '#23e2ff',
            '1412900000': '#33ccff',
            '4410100000': '#42bbff',
            '4410300000': '#b8e2fd',
            '4410500000': '#51a9ff',
            '4411000000': '#33ccff',
            '4411200000': '#42bbff',
            '4411400000': '#4282ff',
            '4411600000': '#23e2ff',
            '4411800000': '#b8e2fd',
            '4412100000': '#51a9ff',
            '4412300000': '#42bbff',
            '4412500000': '#33ccff',
            '4412700000': '#4282ff',
            '4412900000': '#23e2ff',
            '4413100000': '#b8e2fd',
            '4420300000': '#33ccff',
            '4420600000': '#42bbff',
            '4420900000': '#23e2ff',
            '4421400000': '#51a9ff',
            '4421600000': '#4282ff',
            '4422200000': '#b8e2fd',
            '4422500000': '#23e2ff',
            '4422800000': '#51a9ff',
            '4423100000': '#b8e2fd',
            '4423300000': '#33ccff',
            '4423600000': '#4282ff',
            '4423800000': '#42bbff',
            '4424000000': '#42bbff',
            '4424200000': '#33ccff',
            '4424500000': '#23e2ff',
            '4424800000': '#4282ff',
            '4425100000': '#51a9ff',
            '4425400000': '#b8e2fd'
        }
    };

    // return createConfig(clusters, data_url, null);
    // d3.queue()
    //     .defer(d3.json, "../clusters/?format=json")
    //     .defer(d3.json, '../alerts/?format=json')
    //     .await(createConfig);
    //
    // return config;
}

