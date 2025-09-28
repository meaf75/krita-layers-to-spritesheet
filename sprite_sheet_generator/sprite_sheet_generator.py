from krita import Krita

def start():
  application = Krita.instance()
  currentDoc = application.activeDocument()
  activeWindow = application.activeWindow()
  view = activeWindow.activeView()


  w: int = currentDoc.width()
  h: int = currentDoc.height()
  selectedNodes = view.selectedNodes()
  numSelectedNodes : int = len(selectedNodes)
  print("w: {}, h: {}, total: {}".format(w,h, numSelectedNodes))

  # Create new document to store the spritesheet
  newDocument = application.createDocument(
    w*numSelectedNodes, 
    h, 
    "{}_spritesheet".format(currentDoc.name()), 
    currentDoc.colorModel(),
    currentDoc.colorDepth(),
    currentDoc.colorProfile(),
    currentDoc.resolution()
  )
  
  for idx, node in enumerate(selectedNodes):
    # Clone layer data
    newNode = newDocument.createNode(node.name(), "paintlayer")

    # Content of the layer, start from zero to ignore pixels out of the layer
    if node.type() != "paintlayer":
      pixelData = node.projectionPixelData(0,0,w,h) # For non paint layers (like filter layers)
    else:
      pixelData = node.pixelData(0,0,w,h)

    newNode.setPixelData(pixelData,0,0,w,h) # Write data to the new layer
    
    # Reposition node
    newNode.move(idx * w, 0)
    added = newDocument.rootNode().addChildNode(newNode, None)
    print("Added {}: {}".format(newNode.name(),added))
       
  newDocument.nodeByName("Background").remove() # .setVisible(False) # Hide background layer
  activeWindow.addView(newDocument)

# start()