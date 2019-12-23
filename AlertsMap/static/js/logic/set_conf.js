function setConf(data_url, full_access, lang, colors, oblasts) {

    const tiles_list = {
        ru: 'https://api.mapbox.com/styles/v1/denysboiko/cj31bg47c00072rqpzul3t1qb/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        uk: 'https://api.mapbox.com/styles/v1/denysboiko/cj31bi4rk000b2socgh8kzaeu/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        en: 'https://api.mapbox.com/styles/v1/denysboiko/cj1hz2pno004g2qk8fbfwqrtc/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZGVueXNib2lrbyIsImEiOiJjaXpxdzlxMGswMHMzMnFxbzdpYjJoZDN1In0.O3O4iBtTiODWN0C8oGOBwg',
        osm: 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png'
    };

    return {
        map: {
            tiles: tiles_list[lang]
            , center: [48.1, 38.2]
            , zoom: 8
            , minZoom: 6
            , maxZoom: 18
            , maxBounds: [
                [
                    44 - 2,
                    22
                ] // south coords of ukraine + space to bottom datepicker, Ukraine west
                ,
                [
                    53 + 4,
                    41 + 16
                ] // Ukraine north + some space to popups, east coords of ukraine + space to make center near Donetsk/Luhansk on minZoom
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
                    alertID: 'id'
                    , pcode: 'pcode'
                    , settlement: 'settlement'
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
            {key: gettext('Resolved'), text: gettext('Resolved'), color: '#70A800'}
            , {key: gettext('Addressed But Unresolved'), text: gettext('Addressed But Unresolved'), color: '#F69E61'}
            , {key: gettext('Not Addressed'), text: gettext('Not Addressed'), color: '#EE5859'}
        ]
        // , filterCluster: clusters
        , filterOblast: {
            // keyInSourceCode: 'Key data in document'
              donetsk: 'Donetska'
            , luhansk: 'Luhanska'
        }
        , filterOblastRaions: {
              //'http://127.0.0.1:3000/filter/alert_system/Raion/oblast/alert_system/Alert/raion/1400000000/'
              donetsk: oblasts[0]
              //'http://127.0.0.1:3000/filter/alert_system/Raion/oblast/alert_system/Alert/raion/1400000000/'
            , luhansk: oblasts[1]
        }
        , raionColors: colors
    };
}

