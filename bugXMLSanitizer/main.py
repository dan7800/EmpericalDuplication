import sanitize
import monthly_slice as ms


BASE_PATH = '/Users/virginiapujols/Documents/Research Bug Duplication/new_dataset/test/'

sanitize.sanitize_xml_directory(BASE_PATH + '*.xml')
ms.monthly_slice_directory(BASE_PATH + '*.xml')

