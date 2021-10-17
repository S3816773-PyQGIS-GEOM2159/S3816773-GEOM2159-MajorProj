img = QImage (QSize(800,800), QImage.Format_ARGB32_Premultiplied)

color = QColor(255,255,255,255)
img.fill(color.rgba())

p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)

ms = QgsMapSettings()
ms.setBackgroundColor(color)
layer = QgsProject.instance().mapLayersByName('TestLayer')
ms.setLayers([layer[0]])

rect = QgsRectangle(ms.fullExtent())
rect.scale(1.1)
ms.setExtent(rect)

ms.setOutputSize(img.size())

render = QgsMapRendererCustomPainterJob (ms, p)
render.start()
render.waitForFinished()
p.end()

img.save('C:/test_render.png')
print ('image saved')