import httplib
from _Framework.MixerComponent import MixerComponent

from LO2ChannelStripComponent import LO2ChannelStripComponent
from LO2Mixin import LO2Mixin, wrap_init

Color = {
    '16749734': '{"on":true, "sat":104, "bri":255,"hue":64078}',
    '16753961': '{"on":true, "sat":224, "bri":255,"hue":6371}',
    '13408551': '{"on":true, "sat":211, "bri":211,"hue":7281}',
    '16249980': '{"on":true, "sat":127, "bri":249,"hue":10012}',
    '12581632': '{"on":true, "sat":232, "bri":247,"hue":13835}',
    '1769263': '{"on":true, "sat":255, "bri":249,"hue":24393}',
    '2490280': '{"on":true, "sat":255, "bri":252,"hue":29308}',
    '6094824': '{"on":true, "sat":249, "bri":255,"hue":31857}',
    '9160191': '{"on":true, "sat":132, "bri":255,"hue":37500}',
    '5538020': '{"on":true, "sat":186, "bri":226,"hue":38956}',
    '9611263': '{"on":true, "sat":119, "bri":255,"hue":40413}',
    '14183652': '{"on":true, "sat":124, "bri":226,"hue":54066}',
    '15029152': '{"on":true, "sat":160, "bri":239,"hue":60437}',
    '16777215': '{"on":true, "sat":0, "bri":255,"hue":20570}',

    '16725558'  : '{"on":true, "sat":211, "bri":255,"hue":910}',
    '16149507'  : '{"on":true, "sat":255, "bri":255,"hue":4551}',
    '10056267'  : '{"on":true, "sat":135, "bri":158,"hue":5097}',
    '16773172'  : '{"on":true, "sat":204, "bri":255,"hue":10012}',
    '8912743'   : '{"on":true, "sat":145, "bri":252,"hue":20934}',
    '4047616'   : '{"on":true, "sat":226, "bri":191,"hue":21845}',
    '49071'     : '{"on":true, "sat":255, "bri":191,"hue":32039}',
    '1698303'   : '{"on":true, "sat":255, "bri":255,"hue":33677}',
    '1090798'   : '{"on":true, "sat":255, "bri":239,"hue":36044}',
    '32192'     : '{"on":true, "sat":255, "bri":191,"hue":36408}',
    '8940772'   : '{"on":true, "sat":127, "bri":226,"hue":45328}',
    '11958214'  : '{"on":true, "sat":96, "bri":196,"hue":52792}',
    '16726484'  : '{"on":true, "sat":181, "bri":255,"hue":57343}',
    '13684944'  : '{"on":true, "sat":0, "bri":209,"hue":21116}',

    '14837594': '{"on":true, "sat":163, "bri":237,"hue":1274}',
    '16753524': '{"on":true, "sat":142, "bri":255,"hue":3822}',
    '13872497': '{"on":true, "sat":122, "bri":216,"hue":6189}',
    '15597486': '{"on":true, "sat":79, "bri":252,"hue":12924}',
    '13821080': '{"on":true, "sat":81, "bri":226,"hue":13289}',
    '12243060': '{"on":true, "sat":109, "bri":206,"hue":13289}',
    '10208397': '{"on":true, "sat":68, "bri":193,"hue":19842}',
    '13958625': '{"on":true, "sat":45, "bri":252,"hue":26214}',
    '13496824': '{"on":true, "sat":51, "bri":247,"hue":34405}',
    '12173795': '{"on":true, "sat":51, "bri":226,"hue":40777}',
    '13482980': '{"on":true, "sat":43, "bri":226,"hue":48241}',
    '11442405': '{"on":true, "sat":81, "bri":229,"hue":46238}',
    '15064289': '{"on":true, "sat":10, "bri":229,"hue":60255}',
    '11119017': '{"on":true, "sat":0, "bri":168,"hue":21116}',

    '13013643' : '{"on":true, "sat":81, "bri":204,"hue":1274}',
    '12026454' : '{"on":true, "sat":140, "bri":188,"hue":4733}',
    '10060650' : '{"on":true, "sat":81, "bri":155,"hue":5279}',
    '12565097' : '{"on":true, "sat":117, "bri":193,"hue":9648}',
    '10927616' : '{"on":true, "sat":242, "bri":186,"hue":12196}',
    '8237133'  : '{"on":true, "sat":137, "bri":173,"hue":16929}',
    '8962746'  : '{"on":true, "sat":89, "bri":193,"hue":31675}',
    '10204100' : '{"on":true, "sat":58, "bri":196,"hue":36772}',
    '8758722'  : '{"on":true, "sat":89, "bri":193,"hue":37318}',
    '8623052'  : '{"on":true, "sat":99, "bri":204,"hue":40231}',
    '10851765' : '{"on":true, "sat":43, "bri":181,"hue":49151}',
    '12558270' : '{"on":true, "sat":43, "bri":193,"hue":55886}',
    '12349846' : '{"on":true, "sat":104, "bri":193,"hue":60801}',
    '3947580'  : '{"on":true, "sat":0, "bri":122,"hue":21116}',

    '11481907'  : '{"on":true, "sat":191, "bri":183,"hue":546}',
    '11096369'  : '{"on":true, "sat":188, "bri":175,"hue":2912}',
    '7491393'   : '{"on":true, "sat":117, "bri":117,"hue":2912}',
    '14402304'  : '{"on":true, "sat":255, "bri":224,"hue":9284}',
    '8754719'   : '{"on":true, "sat":198, "bri":147,"hue":12196}',
    '5480241'   : '{"on":true, "sat":168, "bri":155,"hue":19660}',
    '695438'    : '{"on":true, "sat":255, "bri":155,"hue":31857}',
    '2319236'   : '{"on":true, "sat":255, "bri":132,"hue":35498}',
    '1716118'   : '{"on":true, "sat":255, "bri":150,"hue":39685}',
    '3101346'   : '{"on":true, "sat":219, "bri":163,"hue":38774}',
    '6441901'   : '{"on":true, "sat":135, "bri":173,"hue":45328}',
    '10701741'  : '{"on":true, "sat":135, "bri":170,"hue":54066}',
    '13381230'  : '{"on":true, "sat":193, "bri":214,"hue":61894}',
    '3947580'   : '{"on":true, "sat":0, "bri":61,"hue":21116}',
        }


class LO2MixerComponent(MixerComponent, LO2Mixin):

    @wrap_init
    def __init__(self, *a, **kw):
        self._track_count = 0
        super(LO2MixerComponent, self).__init__(12, 12, *a, **kw)

        self.add_callback('/live/track/name/block', self._track_name_block)

        self.add_function_callback('/live/tracks', self._lo2_on_track_list_changed)
        self._selected_strip.set_track(None)
        self._selected_strip.set_is_enabled(False)

        self._register_timer_callback(self._update_mixer_vols)


    def _update_mixer_vols(self):
        pass



    def _create_strip(self):
        return LO2ChannelStripComponent()


    def _reassign_tracks(self):
        self.log_message('reassigning tracks')
        diff = len(self.tracks_to_use()) - len(self._channel_strips)

        if diff > 0:
            for i in range(diff):
                self._channel_strips.append(self._create_strip())

        if diff < 0:
                for i in range(len(self._channel_strips)-1, len(self.tracks_to_use())-1, -1):
                    self._channel_strips[i].disconnect()
                    self._channel_strips.remove(self._channel_strips[i])

        for i,cs in enumerate(self._channel_strips):
            cs.set_track(self.tracks_to_use()[i])


        for i,r in enumerate(self._return_strips):
            if i < len(self.song().return_tracks):
                r.set_track(self.song().return_tracks[i])
            else:
                r.set_track(None)


    def _lo2__on_return_tracks_changed(self):
        self._reassign_tracks()



    # Callbacks
    def _lo2_on_track_list_changed(self):
        if len(self.song().tracks) != self._track_count:
            self.log_message('/live/tracks:' + str(len(self.song().tracks)))
            self.send('/live/tracks', len(self.song().tracks))
            self._track_count = len(self.song().tracks)


    def _lo2_on_selected_track_changed(self):
        host = '192.168.1.1:80'
        path = '/api/2gAisFkyMHbIdVlZ5HahrXMh0ODe8IVJ3E9-cg-Z/lights/3/state'
        id, type = self.track_id_type(self.song().view.selected_track)
        body_content = Color[str(self.song().view.selected_track.color)]
        httplib.HTTPConnection(host).request('PUT', path, body_content)

        self.send('/live/track/select', type, id)



    # Track Callbacks
    def _track_name_block(self, msg, src):
        """
        Gets block of scene names
        """
        b = []
        for i in range(msg[2], msg[2]+msg[3]):
            if i < len(self._channel_strips):
                t = self.channel_strip(i)
                b.append(i, t.track_name)
            else:
                b.append(i, '')

        self.send('/live/track/name/block', b)

