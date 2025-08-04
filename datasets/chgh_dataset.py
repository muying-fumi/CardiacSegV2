import os


def get_data_dicts(data_dir):
    #patient_dirs = sorted(os.listdir(data_dir), key=lambda x: int(x.split('_')[-1]))
    patient_dirs = ['pid_30', 'pid_02', 'pid_8', 'pid_9', 'pid_13', 'pid_15', 'pid_20', 'pid_27', 'pid_29','pid_33','pid_34','pid_44','pid_45','pid_100','pid_119','pid_08', 'pid_08_1', 'pid_27', 'pid_31','pid_40','pid_46', 'pid_52', 'pid_56', 'pid_57', 'pid_106','pid_107','pid_108','pid_110','pid_115','pid_140', 'pid_1000', 'pid_1002', 'pid_1003']
    data_dicts = []
    for patient_dir in patient_dirs:
        data_dicts.append({
            "image": os.path.join(os.path.join(data_dir, patient_dir, f'{patient_dir}.nii.gz')),
            "label": os.path.join(os.path.join(data_dir, patient_dir, f'{patient_dir}_gt.nii.gz'))
        })
    return data_dicts
