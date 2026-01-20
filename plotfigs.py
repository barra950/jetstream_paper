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


colunas = read_columns_from_txt('/home/owner/Downloads/control.txt')


colunas = np.array([[float(value) for value in row] for row in colunas])

#dividindo pressao por 100
colunas[12] = colunas[12]/100

#dividindo omega por 100
colunas[7] = colunas[7]/100

#Plotando as variaveis

variaveis = ['u0(iz,1)', 'v0(iz,1)', 'ugeos(iz)', 'uy(iz,1)', 'vy(iz,1)', 'w0(iz)', 'omega(iz)', 'T0(iz,1)', 'Ty(iz,1)', 'Tyy(iz,1)', 'rho(iz)', 'press(iz)', 'P0(iz)', 'Py(iz)', 'Pyy(iz)']   
z = colunas[0]/1000

units = [r'u0 (m $\rms^{-1}$)',r'v0 (m $\rms^{-1}$)',r'ugeos (m $\rms^{-1}$)',r'uy ($\rms^{-1}$)',r'vy ($\rms^{-1}$)',r'w0 (m $\rms^{-1}$)', r'$\mathrm{\omega}$ (hPa s$^{-1}$)','T0 (K)',r'Ty (K $\rmm^{-1}$)',r'Tyy (K $\rmm^{-2}$)',r'$\mathrm{\rho}$ (kg $\rmm^{-3}$)','p (hPa)',r'P0 ($\rmm^{2}$ $\rms^{-2}$ $\rmK^{-1}$)',r'Py (m $\rms^{-2}$ $\rmK^{-1}$)',r'Pyy ($\rms^{-2}$ $\rmK^{-1}$)']


#TEM QUE RODAR DUAS VEZES PQ NA PRIMEIRA DA UM ERRO NO PRIMEIRO PLOT, AS LETRAS FICAM PEQUENAS
for k in range(0,len(variaveis)):
#for k in range(0,2):    
    
    
    fig, ax = plt.subplots(figsize=(12, 15))
    #plt.figtext(0.30, 0.90, "\u263c", fontsize='large', color='y', ha ='right')
    #plt.title(r'U$_\max$ = 5 m $\rms^{-1}$        U$_\min$ = 5 m $\rms^{-1}$',x=0.5, y=1.02)
    plt.rcParams.update({"font.size": 41})
    plt.rcParams['axes.linewidth'] = 2
    ax.plot(colunas[k+1],z,linewidth=5,color='crimson')
    if k == 1:
        ax.plot([0,0],[0,12],color='k',linewidth=2)
    plt.xlabel(units[k])
    plt.ylabel('z (km)')
    plt.ylim([0,12])
    #plt.xlim([290,370])
    ax.grid('True')
    ax.tick_params('both', length=23, width=2, which='major')
    ax.minorticks_on()
    ax.tick_params('both', length=15, width=1, which='minor')
    if k == 3 or k == 4 or k == 5 or k == 6 or k == 8 or k == 13 or k== 14:
        ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
        ax.xaxis.get_major_formatter().set_scientific(True)
        ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
        ax.xaxis.set_tick_params(labeltop=False)
        ax.xaxis.offsetText.set_fontsize(30)
    plt.subplots_adjust(bottom=0.11, top=0.98, hspace=0.15, right=0.95,left=0.15)
    plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/{variaveis[k]}',dpi=100)
    #im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
    #im.show()  
    plt.close()




#Now, doing each plot separately 

#PLot of u and ugeos
fig, ax = plt.subplots(figsize=(12, 15))
#plt.figtext(0.30, 0.90, "\u263c", fontsize='large', color='y', ha ='right')
# plt.title(r'U$_\max$ = 5 m $\rms^{-1}$        U$_\min$ = 5 m $\rms^{-1}$',x=0.5, y=1.02)
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[1],z,linewidth=5,color='crimson',label=variaveis[0])
ax.plot(colunas[3],z,linewidth=5,color='blue',label=variaveis[2],linestyle='--')
plt.xlabel(r'u0 (m $\rms^{-1}$)')
plt.ylabel('z (km)')
ax.legend()
plt.ylim([0,12])
plt.xlim([0,55])
ax.grid('True')
ax.tick_params('both', length=23, width=2, which='major')
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor')
plt.subplots_adjust(bottom=0.11, top=0.98, hspace=0.15, right=0.95,left=0.15)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/{variaveis[0]}_and_{variaveis[2]}',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()



#PLot of uy and vy
fig, ax = plt.subplots(figsize=(12, 15))
#plt.figtext(0.30, 0.90, "\u263c", fontsize='large', color='y', ha ='right')
# plt.title(r'U$_\max$ = 5 m $\rms^{-1}$        U$_\min$ = 5 m $\rms^{-1}$',x=0.5, y=1.02)
plt.rcParams.update({"font.size": 41})
plt.rcParams['axes.linewidth'] = 2
ax.plot(colunas[4],z,linewidth=5,color='crimson',label=variaveis[3])
ax.plot(colunas[5],z,linewidth=5,color='blue',label=variaveis[4],linestyle='--')
ax.plot([0,0],[0,12],color='k',linewidth=2)
plt.xlabel(r'uy, vy ($\rms^{-1}$)')
plt.ylabel('z (km)')
ax.legend()
plt.ylim([0,12])
plt.xlim([-0.000002,0.0000045])
ax.grid('True')
ax.tick_params('both', length=23, width=2, which='major')
ax.minorticks_on()
ax.tick_params('both', length=15, width=1, which='minor')
# ax.ticklabel_format(axis='both', style='sci',scilimits=(0,0),useMathText=True)
# ax.xaxis.get_offset_text().set_fontsize(fontsize=30)
# ax.xaxis.offsetText.set_visible(False)
ax.xaxis.set_major_formatter(plt.matplotlib.ticker.ScalarFormatter(useMathText=True))
ax.xaxis.get_major_formatter().set_scientific(True)
ax.xaxis.get_major_formatter().set_powerlimits((0, 0))
ax.xaxis.set_tick_params(labeltop=False)
ax.xaxis.offsetText.set_fontsize(30)
plt.subplots_adjust(bottom=0.11, top=0.98, hspace=0.15, right=0.95,left=0.15)
plt.savefig(f'/home/owner/Documents/jetstream_paper/figures/{variaveis[3]}_and_{variaveis[4]}',dpi=100)
#im = Image.open('/home/owner/Documents/jetstream_paper/figures/python_figure.png')    
#im.show()  
plt.close()












