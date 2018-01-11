import { h, Component } from 'preact';
import Button from 'preact-material-components/Button';
import 'preact-material-components/Button/style.css';
import style from './style';

export default class Build extends Component {
    state = {
        builds: []
    }
	render({ build }, { }) {
		return (
			<div class={style.build}>
				<h1>Build ID: {build}</h1>
				<p>This is build info for { build }.</p>

				<p>
					<Button raised ripple onClick={' '}>Click Me</Button>
				</p>
			</div>
		);
	}
}
