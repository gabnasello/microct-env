import slicer

def install_slicer_extension(PackageName):
    """
    Install Slicer Extension from terminal
    """

    print("Install " + PackageName + " extension")

    em = slicer.app.extensionsManagerModel()
    
    extensionMetaData = em.retrieveExtensionMetadataByName(PackageName)
    
    if slicer.app.majorVersion*100+slicer.app.minorVersion < 413:
        # Slicer-4.11
        itemId = extensionMetaData["item_id"]
        url = f"{em.serverUrl().toString()}/download?items={itemId}"
        extensionPackageFilename = f"{slicer.app.temporaryPath}/{itemId}"
        slicer.util.downloadFile(url, extensionPackageFilename)
    else:
        # Slicer-4.13
        itemId = extensionMetaData["_id"]
        url = f"{em.serverUrl().toString()}/api/v1/item/{itemId}/download"
        extensionPackageFilename = f"{slicer.app.temporaryPath}/{itemId}"
        slicer.util.downloadFile(url, extensionPackageFilename)
    
    em.installExtension(extensionPackageFilename)


if __name__ == '__main__':

    extension_list= ['SlicerDcm2nii',
                    'Sandbox',
                    'RawImageGuess',
                    'SurfaceWrapSolidify',
                    'MarkupsToModel',
                    'SegmentEditorExtraEffects', 
                    'SlicerIGT',
                    'Auto3dgm',
                    'SlicerMorph']

    for pckg in extension_list:

        install_slicer_extension(pckg)
        
    quit()
