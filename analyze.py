import os
from pathlib import Path

def get_structure(root_dir):
    """Print folder structure in a clean format"""
    root = Path(root_dir)
    
    print("=" * 60)
    print("FOLDER STRUCTURE ANALYSIS")
    print("=" * 60)
    
    # Count files by type
    file_types = {}
    all_files = []
    
    for path in root.rglob('*'):
        if path.is_file():
            ext = path.suffix.lower() if path.suffix else 'no extension'
            file_types[ext] = file_types.get(ext, 0) + 1
            all_files.append(path)
    
    # Print summary
    print("\n📁 ROOT DIRECTORY ITEMS:")
    print("-" * 40)
    for item in sorted(root.iterdir()):
        if item.is_dir():
            print(f"📂 {item.name}/")
        else:
            print(f"📄 {item.name}")
    
    # File type breakdown
    print("\n📊 FILE TYPE BREAKDOWN:")
    print("-" * 40)
    for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True):
        print(f"{ext:15} {count:3} files")
    
    # List all files with paths (relative)
    print("\n📋 ALL FILES WITH RELATIVE PATHS:")
    print("-" * 40)
    for file_path in sorted(all_files):
        rel_path = file_path.relative_to(root)
        print(f"  {rel_path}")
    
    # Special detection for project types
    print("\n🔍 PROJECT TYPE DETECTION:")
    print("-" * 40)
    
    # Check for website files
    web_exts = {'.html', '.htm', '.css', '.js', '.php'}
    web_files = [f for f in all_files if f.suffix.lower() in web_exts]
    
    # Check for PowerShell files
    ps_exts = {'.ps1', '.psm1', '.psd1'}
    ps_files = [f for f in all_files if f.suffix.lower() in ps_exts]
    
    # Check for Python files
    py_files = [f for f in all_files if f.suffix.lower() == '.py']
    
    # Check for config files
    config_exts = {'.json', '.xml', '.yml', '.yaml', '.ini', '.cfg'}
    config_files = [f for f in all_files if f.suffix.lower() in config_exts]
    
    print(f"🌐 Website files: {len(web_files)}")
    print(f"⚡ PowerShell files: {len(ps_files)}")
    print(f"🐍 Python files: {len(py_files)}")
    print(f"⚙️ Config files: {len(config_files)}")
    
    # Suggest separation
    print("\n🎯 SUGGESTED SEPARATION:")
    print("-" * 40)
    if web_files and ps_files:
        print("✅ Found BOTH website AND PowerShell files")
        print("   Should be in SEPARATE repositories!")
    elif web_files:
        print("✅ Mainly website files - keep as one repo")
    elif ps_files:
        print("✅ Mainly PowerShell files - keep as one repo")

if __name__ == "__main__":
    # Automatically use current directory
    current_dir = os.getcwd()
    get_structure(current_dir)
    
    print("\n" + "=" * 60)
    print("Copy everything above this line and paste it to me!")
    print("=" * 60)