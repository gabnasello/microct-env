import slicer

def install_slicer_extension(PackageName):
    """
    Install Slicer Extension from terminal
    
    Function adapted from

    https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/install.sh
    
    """

    print("Install " + PackageName + " extension")
   
    em = slicer.app.extensionsManagerModel()

    if int(slicer.app.revision) >= 30893:
        # Slicer-5.0.3 or later
        em.updateExtensionsMetadataFromServer(True, True)
        if not em.downloadAndInstallExtensionByName(PackageName, True):
            raise ValueError(f"Failed to install {PackageName} extension")
        # Wait for installation to complete
        # (in Slicer-5.4 downloadAndInstallExtensionByName has a waitForComplete flag
        # so that could be enabled instead of running this wait loop)
        import time
        while not em.isExtensionInstalled(PackageName):
            slicer.app.processEvents()
            time.sleep(0.1)


if __name__ == '__main__':

    extension_list= ['SlicerDcm2nii',
                    'Sandbox',
                    'RawImageGuess',
                    'SurfaceWrapSolidify',
                    'MarkupsToModel',
                    'SegmentEditorExtraEffects', 
                    'SlicerIGT',
                    'Auto3dgm',
                    'SlicerMorph',
                    'SegmentMesher']

    for pckg in extension_list:

        install_slicer_extension(pckg)
        
    quit()
