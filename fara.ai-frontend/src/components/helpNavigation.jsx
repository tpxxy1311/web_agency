"use client"
import styles from "@/styles/components/navigation.module.scss"
import { HelpOutlineRounded } from "@mui/icons-material";
import { ChatBubbleOutlineRounded } from "@mui/icons-material";
import { SettingsOutlined } from "@mui/icons-material";
import Link from "next/link";
import { usePathname } from "next/navigation";

const HelpNavigation = () => {
    const pathname = usePathname();
    return ( 
        <nav className={styles.navContainer}>
            <Link href="/help" className={`${styles.linkContainer} ${pathname === '/help' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><HelpOutlineRounded  sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Help</p>
            </Link>
            <Link href="mailto:info@ai-fara.com" className={`${styles.linkContainer} ${pathname === '/feedback' ? styles.active : ''}`}>
            <div className={styles.iconContainer}><ChatBubbleOutlineRounded sx={{ fontSize: 18 }} className={styles.icon}/> </div> <p>Feedback</p>
            </Link>
            <Link href="/settings" className={`${styles.linkContainer} ${pathname === '/settings' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><SettingsOutlined sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Settings</p>
            </Link>
        </nav>
     );
}
 
export default HelpNavigation;