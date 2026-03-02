import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def read_columns_from_txt(file_path):
    """
    Read a text file and create lists for each column.
    
    Parameters:
    file_path (str): Path to the text file
    
    Returns:
    list: List of column lists in order
    """
    column_lists = []
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Remove empty lines and trailing newlines
        data_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:  # Skip empty lines
                data_lines.append(stripped_line)
        
        if not data_lines:
            print("Error: File is empty or contains only whitespace.")
            return []
        
        # Split each line into columns (whitespace-separated)
        split_data = []
        for line in data_lines:
            parts = line.split()  # Split on any whitespace
            split_data.append(parts)
        
        # Find the maximum number of columns in any row
        max_columns = max(len(row) for row in split_data)
        
        # Initialize column lists
        column_lists = [[] for _ in range(max_columns)]
        
        # Fill column lists
        for row in split_data:
            for col_index in range(max_columns):
                if col_index < len(row):
                    column_lists[col_index].append(row[col_index])
                else:
                    column_lists[col_index].append("")  # Fill missing values with empty string
        
        # Print summary
        print(f"Successfully read {len(data_lines)} rows and {max_columns} columns")
        
        # Show preview of data
        print("\nFirst few rows of data:")
        for i in range(min(3, len(data_lines))):
            print(f"  Row {i}: {data_lines[i]}")
        
        print("\nFirst few values in each column:")
        for i, col in enumerate(column_lists):
            preview = col[:5] if len(col) > 5 else col
            print(f"  Column {i}: {preview}")
        
        return column_lists
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


#path figures
#path_terms = '/home/owner/Documents/jetstream_paper/forcing terms/'
path_terms = '/home/owner/Documents/jetstream_paper/FW_ revised data files/'


#Forcing terms for u0
colunas = read_columns_from_txt(path_terms + 'u0forcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\rmu_{0}$-eqn terms (m $\rms^{-2}$)',size='49')
ax.xaxis.set_label_coords(0.4, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/u0terms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()


#Forcing terms for v0
colunas = read_columns_from_txt(path_terms + 'v0forcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
ax.plot(colunas[6],z,linewidth=5,label=r'term6') #term6 so funciona dependendo de qual arquivo esta sendo lido
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\rmv_{0}$-eqn terms (m $\rms^{-2}$)',size='49')
ax.xaxis.set_label_coords(0.4, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/v0terms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()



#Forcing terms for uy
colunas = read_columns_from_txt(path_terms + 'uyforcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\rmu_{y}$-eqn terms ($\rms^{-2}$)',size='49')
ax.xaxis.set_label_coords(0.4, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/uyterms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()



#Forcing terms for vy
colunas = read_columns_from_txt(path_terms + 'vyforcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
ax.plot(colunas[6],z,linewidth=5,label=r'term6')
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\rmv_{y}$-eqn terms ($\rms^{-2}$)',size='49')
ax.xaxis.set_label_coords(0.4, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/vyterms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()



#Forcing terms for T0
colunas = read_columns_from_txt(path_terms + 'T0forcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\mathrm{\theta}$$\rm_{0}$-eqn terms (K $\rms^{-1}$)',size='49')
ax.xaxis.set_label_coords(0.4, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/T0terms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()



#Forcing terms for Ty
colunas = read_columns_from_txt(path_terms + 'Tyforcings.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

z = colunas[0]/1000


fig, ax = plt.subplots(figsize=(12, 15))
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,label=r'term1')
ax.plot(colunas[2],z,linewidth=5,label=r'term2')
ax.plot(colunas[3],z,linewidth=5,label=r'term3')
ax.plot(colunas[4],z,linewidth=5,label=r'term4')
ax.plot(colunas[5],z,linewidth=5,label=r'term5')
#ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'$\mathrm{\theta}$$\rm_{y}$-eqn terms (K $\rmm^{-1}$ $\rms^{-1}$)',size='49')
ax.xaxis.set_label_coords(0.3, -0.07)  # x=0 is left edge, adjust y as needed
plt.ylabel('z (km)',size='49')
ax.legend()
plt.ylim([0,12])
#plt.xlim([-0.000002,0.0000045])
ax.grid('True',color='k')
ax.tick_params('both', length=23, width=2, which='major',top=True, right=True, bottom=True, left=True)
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor',top=True, right=True, bottom=True, left=True)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(41)
plt.subplots_adjust(bottom=0.123, top=0.97, hspace=0.15, right=0.95,left=0.16)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/forcing_figs/Tyterms',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()












