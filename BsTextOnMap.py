#MadeBySobyDamn
import bs
from bsMap import *
import bsMap

def __init__(self, vrOverlayCenterOffset=None):
        """
        Instantiate a map.
        """
        import bsInternal
        bs.Actor.__init__(self)
        self.preloadData = self.preload(onDemand=True)
        def text():
                #bySoby
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue043Writing Mutliple Texts On Screen\ue043\n for Your Server',
                              'scale':1.2,
                              'maxWidth':0,
                              'position':(0,138),
                              'shadow':0.5,
                              'flatness':1.0,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{0: 0.0,500: 1.0,6500: 1.0,7000: 0.0})
                bs.gameTimer(7000,t.delete)
                ##
                t = bs.newNode('text',
                       attrs={ 'text':'Your Second Text YouCan change Line \nif long Message\nLike This!',
                              'scale':1.3,
                              'maxWidth':0,
                              'position':(0,138),
                              'shadow':0.5,
                              'flatness':0.0,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{8500: 0.0,9000: 1.0,14500: 1.0,15000: 0.0})
                bs.gameTimer(15000,t.delete)
                #bySoby
                t = bs.newNode('text',
                       attrs={ 'text':'Your 3rd Message Can add BS Icon using unicodes',
                              'scale':1.2,
                              'maxWidth':0,
                              'position':(0,138),
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'shadow':0.5,
                              'flatness':1.0,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{17500: 0.0,18500: 1.0,24500: 1.0,25000: 0.0})
                bs.gameTimer(25000,t.delete)
                #bySoby
                t = bs.newNode('text',
                       attrs={ 'text':u'\ue043Fourth Text using icones in text -> \ue043',
                              'scale':1.2,
                              'maxWidth':0,
                              'position':(0,139),
                              'shadow':0.5,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'flatness':0.0,
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{27000: 0.0,27500: 1.0,33500: 1.0,34000: 0.0})
                bs.gameTimer(34000,t.delete)
                t = bs.newNode('text',
                       attrs={ 'text':'Your 5th Text',
                              'scale':1.2,
                              'maxWidth':0,
                              'position':(0,138),
                              'shadow':0.5,
                              'flatness':1.0,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{36000: 0.0,36500: 1.0,42500: 1.0,43000: 0.0})
                bs.gameTimer(43000,t.delete)
                ##
                t = bs.newNode('text',
                       attrs={ 'text':'Your 6th Text',
                               'scale':1.2,
                              'maxWidth':0,
                              'position':(0,138),
                              'shadow':0.5,
                              'flatness':1.0,
                              'color':((0+random.random()*1.0),(0+random.random()*1.0),(0+random.random()*1.0)),
                              'hAlign':'center',
                              'vAttach':'bottom'})
                bs.animate(t,'opacity',{45000: 0.0,45500: 1.0,50500: 1.0,51000: 0.0})
                bs.gameTimer(51000,t.delete)
        bs.gameTimer(3500,bs.Call(text))
        bs.gameTimer(56000,bs.Call(text),repeat = True)
        
        # set some defaults
        bsGlobals = bs.getSharedObject('globals')
        # area-of-interest bounds
        aoiBounds = self.getDefBoundBox("areaOfInterestBounds")
        if aoiBounds is None:
            print 'WARNING: no "aoiBounds" found for map:',self.getName()
            aoiBounds = (-1,-1,-1,1,1,1)
        bsGlobals.areaOfInterestBounds = aoiBounds
        # map bounds
        mapBounds = self.getDefBoundBox("levelBounds")
        if mapBounds is None:
            print 'WARNING: no "levelBounds" found for map:',self.getName()
            mapBounds = (-30,-10,-30,30,100,30)
        bsInternal._setMapBounds(mapBounds)
        # shadow ranges
        try: bsGlobals.shadowRange = [
                self.defs.points[v][1] for v in 
                ['shadowLowerBottom','shadowLowerTop',
                 'shadowUpperBottom','shadowUpperTop']]
        except Exception: pass
        # in vr, set a fixed point in space for the overlay to show up at..
        # by default we use the bounds center but allow the map to override it
        center = ((aoiBounds[0]+aoiBounds[3])*0.5,
                  (aoiBounds[1]+aoiBounds[4])*0.5,
                  (aoiBounds[2]+aoiBounds[5])*0.5)
        if vrOverlayCenterOffset is not None:
            center = (center[0]+vrOverlayCenterOffset[0],
                      center[1]+vrOverlayCenterOffset[1],
                      center[2]+vrOverlayCenterOffset[2])
        bsGlobals.vrOverlayCenter = center
        bsGlobals.vrOverlayCenterEnabled = True
        self.spawnPoints = self.getDefPoints("spawn") or [(0,0,0,0,0,0)]
        self.ffaSpawnPoints = self.getDefPoints("ffaSpawn") or [(0,0,0,0,0,0)]
        self.spawnByFlagPoints = (self.getDefPoints("spawnByFlag")
                                  or [(0,0,0,0,0,0)])
        self.flagPoints = self.getDefPoints("flag") or [(0,0,0)]
        self.flagPoints = [p[:3] for p in self.flagPoints] # just want points
        self.flagPointDefault = self.getDefPoint("flagDefault") or (0,1,0)
        self.powerupSpawnPoints = self.getDefPoints("powerupSpawn") or [(0,0,0)]
        self.powerupSpawnPoints = \
            [p[:3] for p in self.powerupSpawnPoints] # just want points
        self.tntPoints = self.getDefPoints("tnt") or []
        self.tntPoints = [p[:3] for p in self.tntPoints] # just want points
        self.isHockey = False
        self.isFlying = False
        self._nextFFAStartIndex = 0
        
bsMap.Map.__init__ = __init__
